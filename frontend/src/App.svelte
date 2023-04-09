<script>
  import Router from 'svelte-spa-router'
  import Hoem  from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from "./routes/QuestionCreate.svelte"
  import Navigation from "./components/Navigation.svelte"
  import UserCreate from "./routes/UserCreate.svelte"

  const routes = {
    '/': Hoem,
    '/detail/:question_id' : Detail,
    '/question-create': QuestionCreate,
    '/user-create': UserCreate,
  }
</script>

<Navigation />
<Router {routes}/>