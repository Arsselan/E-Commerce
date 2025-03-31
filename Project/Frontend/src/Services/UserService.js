// edited by Yannic
// edited by Miles Sasportas
//logout edited by Wael Hourani
import { ApiService } from "./ApiService";
import Cookies from "js-cookie";

class UserService extends ApiService {
    constructor() {
        super();
    }

    async login(username, password) {
        
        const responseOG = await this.axios.post("login", {
            username: username,
            password: password,
            email: username,
        });
    
        const responseSimpleJwt = await this.axios.post("token/", {
            username: username,
            password: password,
            email: username,
        });

        const { access, refresh } = responseSimpleJwt.data;

        // Set cookies for tokens with httponly flag
        Cookies.set("jwt", responseOG.data, { sameSite: "strict", secure: true });
        Cookies.set("access_token", access, { sameSite: "strict", secure: true });
        Cookies.set("refresh_token", refresh, { sameSite: "strict", secure: true });
        super.initializeAxios();

        return responseOG.data;
    }

    async logout() {
        try {
            // Clear cookies and perform other logout logic
            Cookies.remove("jwt");
            Cookies.remove("access_token");
            Cookies.remove("refresh_token");

            // Call your backend API to perform logout
            await this.axios.post("logout");

            // Ensure that Axios is re-initialized without tokens
            super.initializeAxios();
        } catch (error) {
            console.error('Error during logout:', error);
        }
    }

    async getCurrentUser() {
        const response = await this.axios.get("user");
        return response.data;
    }

    async register(user) {
        const response = await this.axios.post("register", user);
        return response.data;
    }

    async getUserData() {
        // Assuming your API endpoint for fetching user data is /users/{userId}
        // const response = await this.axios.get(`/signup/${userId}`);
        const response = await this.axios.get(`/user`);
        return response.data;
    }

    async verifyMail(email) {
        const response = await this.axios.get(`/register/email_validation/`, {
            params: {
                email: email,
            }
        });
        return response.data;
    }
}

export default new UserService();
