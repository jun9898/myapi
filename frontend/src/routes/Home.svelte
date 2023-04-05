<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let question_list = []

    function get_question_list() {
    // fetch("http://127.0.0.1:8000/api/question/list").then((response) => {
    //   response.json().then((json) => { ----------api.js의 fastapi 함수를 사용해서 코드를 수정하였다 fastapi의 대한 이해가 좀 더 필요할 것 같다.
        fastapi('get', '/api/question/list', {}, (json) => {
        question_list = json;
        })
    }
  

    get_question_list()
</script>

<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr>
            <td>{i+1}</td>
            <td>
                <a use:link href="/detail/{question.id}">{question.subject}</a>
            </td>
            <td>{question.create_date}</td>
        </tr>
        {/each}
        </tbody>
    </table>
</div>
