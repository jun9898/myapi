import { writable } from "svelte/store";

const persist_storage = (key, initValue) => {   //persist_storage 함수는 이름(key)과 초기값(initValue) 를 입력받아 writable 스토어를 생성하여 리턴하는 함수이다.
    const storedValueStr = localStorage.getItem(key)
    const store = writable(storedValueStr !=null ? JSON.parse(storedValueStr): initValue)
    store.subscribe((val) => { localStorage.setItem(key,JSON.stringify(val))
    })
    return store
}

export const page = persist_storage("page", 0)
export const access_token = persist_storage("access_token", "")
export const username = persist_storage("username", "")
export const is_login = persist_storage("is_login", false)
