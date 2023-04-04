<script>
  import Router from 'svelte-spa-router'
  import Hoem  from './routes/Hoem.svelte'

  const routes = {
    '/': Hoem,
  }
</script>

<Router {routes}/>