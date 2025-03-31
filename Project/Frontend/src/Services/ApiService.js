// edited by Yannic
// edited by Miles Sasportas
import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import Cookies from "js-cookie";


window.axios = require('axios');

window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
let token = document.head.querySelector('meta[name="csrf-token"]');

if (token) {
    window.axios.defaults.headers.common['X-CSRF-TOKEN'] = token.content;
} else {
    console.error('CSRF token not found: https://laravel.com/docs/csrf#csrf-x-csrf-token');
}

class ApiService {
    constructor() {
        this.initializeAxios();
    }

    async initializeAxios() {
        this.axios = axios.create({
            baseURL: `https://localhost:8000/api/`,
            headers: {},
            withCredentials: true,
        });

        await this.setupAuthTokens();
    }
        
    async setupRefresh() {
        if (this.refreshTimerId) {
            // Alten timer stoppen
            clearInterval(this.refreshTimerId);
            this.refreshTimerId = 0;
        }

        createAuthRefreshInterceptor(
            this.axios,
            async () => this.setupAuthTokens()
        );

        this.refreshTimerId = setInterval(async () => await this.refreshAuthToken(), 5 * 60 * 1000 /* 5 min */);
    }

    
    async refreshAuthToken() {
        const refresh_token = Cookies.get("refresh_token");
        const refresh_tokenIsSet = refresh_token && refresh_token !== "undefined" /* Frag mich nicht wieso 'undefined' gespeichert war */;
        if (!refresh_tokenIsSet) {
            // Noch nicht eingeloggt gewesen
            return;
        }

        try {
            const response = await this.axios.post("token/refresh/", {
                refresh: refresh_token,
            });

            const new_access_token = response.data.access;
            Cookies.set("access_token", new_access_token, { sameSite: "strict", secure: true });
            this.axios.defaults.headers.common["Authorization"] = `Bearer ${new_access_token}`;
        } catch (error) {
            console.error("Error refreshing token:", error);
            throw error;
        }
    }


    async setupAuthTokens() {
        const token = Cookies.get("access_token");
        const tokenIsSet = token && token !== "undefined" /* Frag mich nicht wieso 'undefined' gespeichert war */;

        if(tokenIsSet) {
            // Add the header
            this.axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
        }
        else {
            await this.refreshAuthToken();
        }

        await this.setupRefresh();
    }

    isDevelopment = false;
    refreshTimerId = 0;
}

export default new ApiService();
export { ApiService };