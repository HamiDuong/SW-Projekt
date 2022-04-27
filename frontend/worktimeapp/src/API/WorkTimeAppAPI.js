//Alle BOs importieren

export default class WorkTimeAppAPI{
    static #api = null

    #worktimeappServerBaseURL = '/api';

    //Hier alle URL Zuweisungen

    static getAPI(){
        if(this.#api == null){
            this.#api = new WorkTimeAppAPI();
        }
        return this.#api;
    }

    #fetchAdvanced = (url, init) => fetch(url, init).then(
        res => {
            if(!res.ok){
                throw Error(`${res.status} ${res.statusText}`);
            }
            return res.json();
        }
    )

    //Hier alle Methoden vom Backend in Frontend ziehen
}