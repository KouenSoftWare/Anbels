<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">首页</router-link> |
      <router-link to="/strategy">策略模块</router-link> |
      <router-link to="/notice">通知渠道</router-link> |
      <router-link to="/about">关于我们</router-link>
    </div>
    <router-view/>
  </div>
</template>

<style lang="stylus">
#app
  font-family 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50
  a
    color #000
    font-weight bold
  a:hover
    color #1c7fff
    font-weight bold
</style>
