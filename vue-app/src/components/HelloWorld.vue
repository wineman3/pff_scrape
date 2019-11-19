<template>
  <div>
    <p>
      <label for="playerName">Player Name</label>
      <input id="name" v-model="name" type="text" name="name" />
    </p>
    <p v-if="grade">Overall grade: {{ grade }}</p>
    <p>
      <button name="search" @click="search(name)">Search</button>
    </p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      name: "",
      grade: ""
    };
  },
  methods: {
    search(name) {
      // eslint-disable-next-line no-console
      console.log(`search for player: ${name}`);
      // const path = "http://localhost:5000/api/test";
      // axios.get(path, {
      //   params: {
      //     playerName: name
      //   }
      // })
      const playerName = name.replace(' ', '_');
      const path = `https://2kjhnzj1oi.execute-api.us-east-1.amazonaws.com/dev/grade/${playerName}`;
      axios.get(path)
      .then(response => {
        // eslint-disable-next-line no-console
        console.log(response.data);
        this.grade = response.data;
      })
      .catch(error => {
        // eslint-disable-next-line no-console
        console.log(error)
      })
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
