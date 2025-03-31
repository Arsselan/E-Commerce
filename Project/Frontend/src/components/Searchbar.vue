<!-- edited by Yannic-->
<!-- edited by Miles Sasportas-->
<!--author <Arsselan-->
<template>
  <v-menu
    v-model="isDropdownOpen"
    :class="{ 'custom-menu-class': isDropdownOpen }"
    @click:outside="closeDropdown"
  >
    <template v-slot:activator="{}">
      <v-text-field
        ref="searchField"
        placeholder="Search"
        v-model="searchString"
        style="width: 200px;height: 50px;"
        hide-details
        append-icon="mdi-magnify"
        clearable
        variant="outlined"
        @click="openDropdown"
        @keydown:enter.stop.prevent="search"
        @click:append="search"
      ></v-text-field>
    </template>

    <v-list>
      <v-list-item v-for="(item, index) in searchHistory" :key="index" @click="selectDropdownItem(item)">
        <v-list-item-content>
          <v-list-item-title>{{ item }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-menu>
</template>
<!--author <Arsselan-->
<script>
export default {
  name: 'searchbar',
  data() {
    return {
      searchString: "",
      isDropdownOpen: false,
      searchHistory: [],
    };
  },
  methods: {
    search() {
      this.$router.push({
        name: "Home",
        query: {
          query: this.searchString,
        }
      });
      this.addToSearchHistory(this.searchString);
    },
    openDropdown() {
      this.loadSearchHistory();
      this.isDropdownOpen = true;
    },
    closeDropdown() {
      this.isDropdownOpen = false;
    },
    selectDropdownItem(item) {
      this.searchString = item;
      this.search();
      this.closeDropdown();
    },
    addToSearchHistory(term) {
      // Add term to search history
      if (this.searchHistory.length >= 4) {
        this.searchHistory.pop(); // Remove oldest entry if max size reached
      }
      this.searchHistory.unshift(term); // Add new entry to the beginning
      this.saveSearchHistory();
    },
    loadSearchHistory() {
      // Load search history from local storage
      const storedHistory = localStorage.getItem('searchHistory');
      if (storedHistory) {
        this.searchHistory = JSON.parse(storedHistory).slice(0, 4); // Load only the latest four entries
      }
    },
    saveSearchHistory() {
      // Save search history to local storage
      localStorage.setItem('searchHistory', JSON.stringify(this.searchHistory));
    },
  },
};
</script>

<style scoped>
.custom-menu-class {
  top: 80px; /* Ändere den Wert je nach gewünschtem Abstand */
  margin-left: 950px;
  margin-right: 100px;
}
</style>
