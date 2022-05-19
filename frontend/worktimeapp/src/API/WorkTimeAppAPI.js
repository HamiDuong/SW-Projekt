//Alle BOs importieren
import TimeIntervalBO from './TimeIntervalBO'
import BreakBO from './GroupBO';
import IllnessBO from './IllnessBO';
import ProjectDurationBO from './ProjectDurationBO';
import ProjectWorkBO from './ProjectWorkBO';
import VacationBO from './VacationBO';
import WorkBO from './WorkBO';

export default class WorkTimeAppAPI{
    static #api = null

    #worktimeappServerBaseURL = '/api';

    //Hier alle URL Zuweisungen

    //TimeInterval

    //Break

    //Illness

    //ProjectDuration

    //ProjectWork

    //Vacation

    //Work

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