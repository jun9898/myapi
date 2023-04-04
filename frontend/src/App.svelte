<script>
  import Router from 'svelte-spa-router'
  import Hoem  from './routes/Home.svelte'

  const routes = {
    '/': Hoem,
  }
</script>

<Router {routes}/>