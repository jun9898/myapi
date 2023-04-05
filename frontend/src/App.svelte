<script>
  import Router from 'svelte-spa-router'
  import Hoem  from './routes/Home.svelte'
  import Detail from "./routes/Detail.svelte"

  const routes = {
    '/': Hoem,
    '/detail/:question_id' : Detail,
  }
</script>

<Router {routes}/>