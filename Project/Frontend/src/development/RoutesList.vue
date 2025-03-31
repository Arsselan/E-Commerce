<!-- edited by Miles Sasportas-->
<template>
  <v-list style="background-color: #f5f5f5;">
    <div class="d-flex">
      <v-list-item
        v-for="(item, i) in existingRoutes"
        :key="i"
        class="mr-2"
      >
        <router-link :to="item.path">
          {{ item.name }}
        </router-link>
      </v-list-item>
    </div>
  </v-list>

</template>

<script>
import { routes } from "../router/index";

export default  {
    name: 'routes-list',
    components: {

    },
    props: {

    },
    data () {
        return {
          existingRoutes: routes,
        }
    },
    methods: {

    },
    computed: {

    },
}


</script>

<style scoped>
  .routes-list {

  }
</style>
