//Alle BOs importieren
import TimeIntervalBO from './TimeIntervalBO'
import BreakBO from './BreakBO';
import IllnessBO from './IllnessBO';
import ProjectDurationBO from './ProjectDurationBO';
import ProjectWorkBO from './ProjectWorkBO';
import VacationBO from './VacationBO';
import WorkBO from './WorkBO';
import BookingBO from './BookingBO';
import TimeIntervalBookingBO from './TimeIntervalBookingBO';

export default class WorkTimeAppAPI {
    static #api = null

    #worktimeappServerBaseURL = 'http://127.0.0.1:5000/worktimeapp';

    //Hier alle URL Zuweisungen
    // # = () => `${this.#worktimeappServerBaseURL}/`;

    //TimeInterval
    #getTimeIntervalURL = (id) => `${this.#worktimeappServerBaseURL}/timeinterval/${id}`;
    #getAllTimeIntervalsURL = () => `${this.#worktimeappServerBaseURL}/timeinterval`;
    #addTimeIntervalURL = () => `${this.#worktimeappServerBaseURL}/timeinterval`;
    #deleteTimeIntervalURL = (id) => `${this.#worktimeappServerBaseURL}/timeinterval/${id}`;
    #updateTimeIntervalURL = (id) => `${this.#worktimeappServerBaseURL}/timeinterval/${id}`;
    #getTimeIntervalByTypeURL = (type) => `${this.#worktimeappServerBaseURL}/timeintervaltype/${type}`;

    //Break
    #getBreakURL = (id) => `${this.#worktimeappServerBaseURL}/break/${id}`;
    #getAllBreaksURL = () => `${this.#worktimeappServerBaseURL}/break`;
    #addBreakURL = () => `${this.#worktimeappServerBaseURL}/break`;
    #deleteBreakURL = (id) => `${this.#worktimeappServerBaseURL}/break/${id}`;
    #updateBreakURL = (id) => `${this.#worktimeappServerBaseURL}/break/${id}`;
    #getBreakByDateURL = (date) => `${this.#worktimeappServerBaseURL}/breakdate/${date}`;
    #getBreakByPeriodURL = (start, end) => `${this.#worktimeappServerBaseURL}/breakperiod/${start}/${end}`;

    //Illness
    #getIllnessURL = (id) => `${this.#worktimeappServerBaseURL}/illness/${id}`;
    #getAllIllnessesURL = () => `${this.#worktimeappServerBaseURL}/illness`;
    #addIllnessURL = () => `${this.#worktimeappServerBaseURL}/illness`;
    #deleteIllnessURL = (id) => `${this.#worktimeappServerBaseURL}/illness/${id}`;
    #updateIllnessURL = (id) => `${this.#worktimeappServerBaseURL}/illness/${id}`;
    #getIllnessByDateURL = (date) => `${this.#worktimeappServerBaseURL}/illnessdate/${date}`;
    #getIllnessByPeriodURL = (start, end) => `${this.#worktimeappServerBaseURL}/illnessperiod/${start}/${end}`;

    //ProjectDuration
    #getProjectDurationURL = (id) => `${this.#worktimeappServerBaseURL}/projectduration/${id}`;
    #getAllProjectDurationsURL = () => `${this.#worktimeappServerBaseURL}/projectduration`;
    #addProjectDurationURL = () => `${this.#worktimeappServerBaseURL}/projectduration`;
    #deleteProjectDurationURL = (id) => `${this.#worktimeappServerBaseURL}/projectduration/${id}`;
    #updateProjectDurationURL = (id) => `${this.#worktimeappServerBaseURL}/projectduration/${id}`;
    #getProjectDurationByDateURL = (date) => `${this.#worktimeappServerBaseURL}/projectdurationdate/${date}`;
    #getProjectDurationByPeriodURL = (start, end) => `${this.#worktimeappServerBaseURL}/projectdurationperiod/${start}/${end}`;
    #getProjectDurationByProjectURL = (id) => `${this.#worktimeappServerBaseURL}/projectdurationproject/${id}`;

    //ProjectWork
    #getProjectWorkURL = (id) => `${this.#worktimeappServerBaseURL}/projectwork/${id}`;
    #getAllProjectWorksURL = () => `${this.#worktimeappServerBaseURL}/projectwork`;
    #addProjectWorkURL = () => `${this.#worktimeappServerBaseURL}/projectwork`;
    #deleteProjectWorkURL = (id) => `${this.#worktimeappServerBaseURL}/projectwork/${id}`;
    #updateProjectWorkURL = (id) => `${this.#worktimeappServerBaseURL}/projectwork/${id}`;
    #getProjectWorkByDateURL = (date) => `${this.#worktimeappServerBaseURL}/projectworkdate/${date}`;
    #getProjectWorkByPeriodURL = (start, end) => `${this.#worktimeappServerBaseURL}/projectworkperiod/${start}/${end}`;
    #getProjectWorkByActivityURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkactivity/${id}`;

    //Vacation
    #getVacationURL = (id) => `${this.#worktimeappServerBaseURL}/vacation/${id}`;
    #getAllVacationsURL = () => `${this.#worktimeappServerBaseURL}/vacation`;
    #addVacationURL = () => `${this.#worktimeappServerBaseURL}/vacation`;
    #deleteVacationURL = (id) => `${this.#worktimeappServerBaseURL}/vacation/${id}`;
    #updateVacationURL = (id) => `${this.#worktimeappServerBaseURL}/vacation/${id}`;
    #getVacationByDateURL = (date) => `${this.#worktimeappServerBaseURL}/vacationdate/${date}`;
    #getVacationByPeriodURL = (start, end) => `${this.#worktimeappServerBaseURL}/vacationperiod/${start}/${end}`;

    //Work
    #getWorkURL = (id) => `${this.#worktimeappServerBaseURL}/work/${id}`;
    #getAllWorksURL = () => `${this.#worktimeappServerBaseURL}/work`;
    #addWorkURL = () => `${this.#worktimeappServerBaseURL}/work`;
    #deleteWorkURL = (id) => `${this.#worktimeappServerBaseURL}/work/${id}`;
    #updateWorkURL = (id) => `${this.#worktimeappServerBaseURL}/work/${id}`;
    #getWorkByDateURL = (date) => `${this.#worktimeappServerBaseURL}/workdate/${date}`;
    #getWorkByPeriodURL = (start, end) => `${this.#worktimeappServerBaseURL}/workperiod/${start}/${end}`;

    //Booking URLS
    #addTimeIntervalBookingURL = () => `${this.#worktimeappServerBaseURL}/booking/timeintervalbooking`

    //Beginn aller Event-BOs

    //Event
    #getEventURL = (id) => `${this.#worktimeappServerBaseURL}/event/${id}`;
    #getAllEventesURL = () => `${this.#worktimeappServerBaseURL}/events`;
    #addEventURL = () => `${this.#worktimeappServerBaseURL}/events`;
    #deleteEventURL = (id) => `${this.#worktimeappServerBaseURL}/event/${id}`;
    #updateEventURL = (id) => `${this.#worktimeappServerBaseURL}/event/${id}`;
    #getAllTypeEvents = (type) => `${this.#worktimeappServerBaseURL}/eventtype/${type}`;

    //BreakStart
    #getBreakStartURL = (id) => `${this.#worktimeappServerBaseURL}/breakstart/${id}`;
    #getAllBreakStartsURL = () => `${this.#worktimeappServerBaseURL}/breakstarts`;
    #addBreakStartURL = () => `${this.#worktimeappServerBaseURL}/breakstart`;
    #deleteBreakStartURL = (id) => `${this.#worktimeappServerBaseURL}/breakstart/${id}`;
    #updateBreakStartURL = (id) => `${this.#worktimeappServerBaseURL}/breakstart/${id}`;
    #getBreakStartByDateURL = (date) => `${this.#worktimeappServerBaseURL}/breakstartdate/${date}`;

    //BreakEnd
    #getBreakEndURL = (id) => `${this.#worktimeappServerBaseURL}/breakend/${id}`;
    #getAllBreakEndsURL = () => `${this.#worktimeappServerBaseURL}/breakends`;
    #addBreakEndURL = () => `${this.#worktimeappServerBaseURL}/breakend`;
    #deleteBreakEndURL = (id) => `${this.#worktimeappServerBaseURL}/breakend/${id}`;
    #updateBreakEndURL = (id) => `${this.#worktimeappServerBaseURL}/breakend/${id}`;
    #getBreakEndByDateURL = (date) => `${this.#worktimeappServerBaseURL}/breakenddate/${date}`;

    //IllnessStart
    #getIllnessStartURL = (id) => `${this.#worktimeappServerBaseURL}/illnessstart/${id}`;
    #getAllIllnessStartesURL = () => `${this.#worktimeappServerBaseURL}/illnessstarts`;
    #addIllnessStartURL = () => `${this.#worktimeappServerBaseURL}/illnessstart`;
    #deleteIllnessStartURL = (id) => `${this.#worktimeappServerBaseURL}/illnessstart/${id}`;
    #updateIllnessStartURL = (id) => `${this.#worktimeappServerBaseURL}/illnessstart/${id}`;
    #getIllnessStartByDateURL = (date) => `${this.#worktimeappServerBaseURL}/illnessstartdate/${date}`;

    //IllnessEnd
    #getIllnessEndURL = (id) => `${this.#worktimeappServerBaseURL}/illnessend/${id}`;
    #getAllIllnessEndesURL = () => `${this.#worktimeappServerBaseURL}/illnessends`;
    #addIllnessEndURL = () => `${this.#worktimeappServerBaseURL}/illnessend`;
    #deleteIllnessEndURL = (id) => `${this.#worktimeappServerBaseURL}/illnessend/${id}`;
    #updateIllnessEndURL = (id) => `${this.#worktimeappServerBaseURL}/illnessend/${id}`;
    #getIllnessEndByDateURL = (date) => `${this.#worktimeappServerBaseURL}/illnessenddate/${date}`;

    //ProjectWorkStart
    #getProjectWorkStartURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkstart/${id}`;
    #getAllProjectWorkStartsURL = () => `${this.#worktimeappServerBaseURL}/projectworkstarts`;
    #addProjectWorkStartURL = () => `${this.#worktimeappServerBaseURL}/projectworkstart`;
    #deleteProjectWorkStartURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkstart/${id}`;
    #updateProjectWorkStartURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkstart/${id}`;
    #getProjectWorkStartByDateURL = (date) => `${this.#worktimeappServerBaseURL}/projectworkstartdate/${date}`;

    //ProjectWorkEnd
    #getProjectWorkEndURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkend/${id}`;
    #getAllProjectWorkEndsURL = () => `${this.#worktimeappServerBaseURL}/projectworkends`;
    #addProjectWorkEndURL = () => `${this.#worktimeappServerBaseURL}/projectworkend`;
    #deleteProjectWorkEndURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkend/${id}`;
    #updateProjectWorkEndURL = (id) => `${this.#worktimeappServerBaseURL}/projectworkend/${id}`;
    #getProjectWorkEndByDateURL = (date) => `${this.#worktimeappServerBaseURL}/projectworkenddate/${date}`;

    //VacationStart
    #getVacationStartURL = (id) => `${this.#worktimeappServerBaseURL}/vacationstart/${id}`;
    #getAllVacationStartsURL = () => `${this.#worktimeappServerBaseURL}/vacationstarts`;
    #addVacationStartURL = () => `${this.#worktimeappServerBaseURL}/vacationstart`;
    #deleteVacationStartURL = (id) => `${this.#worktimeappServerBaseURL}/vacationstart/${id}`;
    #updateVacationStartURL = (id) => `${this.#worktimeappServerBaseURL}/vacationstart/${id}`;
    #getVacationStartByDateURL = (date) => `${this.#worktimeappServerBaseURL}/vacationstartdate/${date}`;

    //VacationEnd
    #getVacationEndURL = (id) => `${this.#worktimeappServerBaseURL}/vacationend/${id}`;
    #getAllVacationEndsURL = () => `${this.#worktimeappServerBaseURL}/vacationends`;
    #addVacationEndURL = () => `${this.#worktimeappServerBaseURL}/vacationend`;
    #deleteVacationEndURL = (id) => `${this.#worktimeappServerBaseURL}/vacationend/${id}`;
    #updateVacationEndURL = (id) => `${this.#worktimeappServerBaseURL}/vacationend/${id}`;
    #getVacationEndByDateURL = (date) => `${this.#worktimeappServerBaseURL}/vacationenddate/${date}`;


    //FlexDayStart
    #getFlexDayStartURL = (id) => `${this.#worktimeappServerBaseURL}/flexdaystart/${id}`;
    #getAllFlexDayStartesURL = () => `${this.#worktimeappServerBaseURL}/flexdaystarts`;
    #addFlexDayStartURL = () => `${this.#worktimeappServerBaseURL}/flexdaystart`;
    #deleteFlexDayStartURL = (id) => `${this.#worktimeappServerBaseURL}/flexdaystart/${id}`;
    #updateFlexDayStartURL = (id) => `${this.#worktimeappServerBaseURL}/flexdaystart/${id}`;
    #getFlexDayStartByDateURL = (date) => `${this.#worktimeappServerBaseURL}/flexdaystartdate/${date}`;

    //FlexDayEnd
    #getFlexDayEndURL = (id) => `${this.#worktimeappServerBaseURL}/flexdayend/${id}`;
    #getAllFlexDayEndsURL = () => `${this.#worktimeappServerBaseURL}/flexdayends`;
    #addFlexDayEndURL = () => `${this.#worktimeappServerBaseURL}/flexdayend`;
    #deleteFlexDayEndURL = (id) => `${this.#worktimeappServerBaseURL}/flexdayend/${id}`;
    #updateFlexDayEndURL = (id) => `${this.#worktimeappServerBaseURL}/flexdayend/${id}`;
    #getFlexDayEndByDateURL = (date) => `${this.#worktimeappServerBaseURL}/flexdayenddate/${date}`;

    //Coming
    #getComingURL = (id) => `${this.#worktimeappServerBaseURL}/coming/${id}`;
    #getAllComingesURL = () => `${this.#worktimeappServerBaseURL}/coming`;
    #addComingURL = () => `${this.#worktimeappServerBaseURL}/coming`;
    #deleteComingURL = (id) => `${this.#worktimeappServerBaseURL}/coming/${id}`;
    #updateComingURL = (id) => `${this.#worktimeappServerBaseURL}/coming/${id}`;
    #getComingByDateURL = (date) => `${this.#worktimeappServerBaseURL}/comingdate/${date}`;

    //Going
    #getGoingURL = (id) => `${this.#worktimeappServerBaseURL}/going/${id}`;
    #getAllGoingesURL = () => `${this.#worktimeappServerBaseURL}/going`;
    #addGoingURL = () => `${this.#worktimeappServerBaseURL}/going`;
    #deleteGoingURL = (id) => `${this.#worktimeappServerBaseURL}/going/${id}`;
    #updateGoingURL = (id) => `${this.#worktimeappServerBaseURL}/going/${id}`;
    #getGoingByDateURL = (date) => `${this.#worktimeappServerBaseURL}/goingdate/${date}`;




    static getAPI() {
        if (this.#api == null) {
            this.#api = new WorkTimeAppAPI();
        }
        return this.#api;
    }

    #fetchAdvanced = (url, init) => fetch(url, init).then(
        res => {
            if (!res.ok) {
                throw Error(`${res.status} ${res.statusText}`);
            }
            return res.json();
        }
    )

    //Hier alle Methoden vom Backend in Frontend ziehen

    //TimeInterval Methoden
    getTimeInterval(timeinterval) {
        return this.#fetchAdvanced(this.#getTimeIntervalURL(timeinterval)).then((responseJSON) => {
            let responseTimeInterval = TimeIntervalBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseTimeInterval)
            })
        })

    }

    getAllTimeInterval() {
        return this.#fetchAdvanced(this.#getAllTimeIntervalsURL()).then((responseJSON) => {
            let responseTimeInterval = TimeIntervalBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseTimeInterval)
            })
        })
    }

    addTimeInterval(timeinterval) {
        return this.#fetchAdvanced(this.#addTimeIntervalURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(timeinterval)
        }).them((responseJSON) => {
            let responseTimeInterval = TimeIntervalBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseTimeInterval)
            })
        })
    }

    deleteTimeInterval(timeinterval) {
        return this.#fetchAdvanced(this.#deleteTimeIntervalURL(timeinterval), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseTimeInterval = TimeIntervalBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseTimeInterval)
            })
        })
    }

    updateTimeInterval(timeinterval) {
        return this.#fetchAdvanced(this.#updateTimeIntervalURL(timeinterval), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(timeinterval)
        }).then((responseJSON) => {
            let responseTimeInterval = TimeIntervalBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseTimeInterval)
            })
        })
    }

    getTimeIntervalByType() {
        return this.#fetchAdvanced(this.#getTimeIntervalByTypeURL()).then((responseJSON) => {
            let responseTimeInterval = TimeIntervalBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseTimeInterval)
            })
        })
    }

    //Break Methoden
    getBreak(br) {
        return this.#fetchAdvanced(this.#getBreakURL(br)).then((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })

    }

    getAllBreak() {
        return this.#fetchAdvanced(this.#getAllBreaksURL()).then((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })
    }

    addBreak(br) {
        return this.#fetchAdvanced(this.#addBreakURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(br)
        }).them((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })
    }

    deleteBreak(br) {
        return this.#fetchAdvanced(this.#deleteBreakURL(br), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })
    }

    updateBreak(br) {
        return this.#fetchAdvanced(this.#updateBreakURL(br), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(br)
        }).then((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })
    }

    getBreakByDate(date) {
        return this.#fetchAdvanced(this.#getBreakByDateURL(date)).then((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })
    }

    getBreakByPeriod(start, end) {
        return this.#fetchAdvanced(this.#getBreakByPeriodURL(start, end)).then((responseJSON) => {
            let responseBreak = BreakBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseBreak)
            })
        })
    }

    //Illness Methoden
    getIllness(illness) {
        return this.#fetchAdvanced(this.#getIllnessURL(illness)).then((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })

    }

    getAllIllness() {
        return this.#fetchAdvanced(this.#getAllIllnessesURL()).then((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })

    }

    addIllness(illness) {
        return this.#fetchAdvanced(this.#addIllnessURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(illness)
        }).them((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })
    }

    deleteIllness(illness) {
        return this.#fetchAdvanced(this.#deleteIllnessURL(illness), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })
    }

    updateIllness(illness) {
        return this.#fetchAdvanced(this.#updateIllnessURL(illness), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(illness)
        }).then((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })
    }

    getIllnessByDate(date) {
        return this.#fetchAdvanced(this.#getIllnessByDateURL(date)).then((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })
    }

    getIllnessByPeriod(start, end) {
        return this.#fetchAdvanced(this.#getIllnessByPeriodURL(start, end)).then((responseJSON) => {
            let responseIllness = IllnessBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseIllness)
            })
        })
    }

    //ProjectDuration Methoden
    getProjectDuration(projectduration) {
        return this.#fetchAdvanced(this.#getProjectDurationURL(projectduration)).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })

    }

    getAllProjectDuration() {
        return this.#fetchAdvanced(this.#getAllProjectDurationsURL()).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })

    }

    addProjectDuration(projectduration) {
        return this.#fetchAdvanced(this.#addProjectDurationURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(projectduration)
        }).them((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })
    }

    deleteProjectDuration(projectduration) {
        return this.#fetchAdvanced(this.#deleteProjectDurationURL(projectduration), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })
    }

    updateProjectDuration(projectduration) {
        return this.#fetchAdvanced(this.#updateProjectDurationURL(projectduration), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(projectduration)
        }).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })
    }

    getProjectDurationByDate(date) {
        return this.#fetchAdvanced(this.#getProjectDurationByDateURL(date)).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })
    }

    getProjectDurationByPeriod(start, end) {
        return this.#fetchAdvanced(this.#getProjectDurationByPeriodURL(start, end)).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })
    }

    getProjectDurationByProject(id) {
        return this.#fetchAdvanced(this.#getProjectDurationByProjectURL(id)).then((responseJSON) => {
            let responseProjectDuration = ProjectDurationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectDuration)
            })
        })
    }

    //ProjectWork Methoden
    getProjectWork(projectwork) {
        return this.#fetchAdvanced(this.#getProjectWorkURL(projectwork)).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })

    }

    getAllProjectWork() {
        return this.#fetchAdvanced(this.#getAllProjectWorksURL()).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })

    }

    addProjectWork(projectwork) {
        return this.#fetchAdvanced(this.#addProjectWorkURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(projectwork)
        }).them((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })
    }

    deleteProjectWork(projectwork) {
        return this.#fetchAdvanced(this.#deleteProjectWorkURL(projectwork), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })
    }

    updateProjectWork(projectwork) {
        return this.#fetchAdvanced(this.#updateProjectWorkURL(projectwork), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(projectwork)
        }).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })
    }

    getProjectWorkByDate(date) {
        return this.#fetchAdvanced(this.#getProjectWorkByDateURL(date)).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })
    }

    getProjectWorkByPeriod(start, end) {
        return this.#fetchAdvanced(this.#getProjectWorkByPeriodURL(start, end)).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })
    }

    getProjectWorkByActivity(id) {
        return this.#fetchAdvanced(this.#getProjectWorkByActivityURL(id)).then((responseJSON) => {
            let responseProjectWork = ProjectWorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseProjectWork)
            })
        })
    }

    //Vacation Methoden
    getVacation(vacation) {
        return this.#fetchAdvanced(this.#getVacationURL(vacation)).then((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })

    }

    getAllVacation() {
        return this.#fetchAdvanced(this.#getAllVacationsURL()).then((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })

    }

    addVacation(vacation) {
        return this.#fetchAdvanced(this.#addVacationURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(vacation)
        }).them((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })
    }

    deleteVacation(vacation) {
        return this.#fetchAdvanced(this.#deleteVacationURL(vacation), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })
    }

    updateVacation(vacation) {
        return this.#fetchAdvanced(this.#updateVacationURL(vacation), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(vacation)
        }).then((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })
    }

    getVacationByDate(date) {
        return this.#fetchAdvanced(this.#getVacationByDateURL(date)).then((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })
    }

    getVacationByPeriod(start, end) {
        return this.#fetchAdvanced(this.#getVacationByPeriodURL(start, end)).then((responseJSON) => {
            let responseVacation = VacationBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseVacation)
            })
        })
    }

    //Work Methoden
    getWork(work) {
        return this.#fetchAdvanced(this.#getWorkURL(work)).then((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })

    }

    getAllWork() {
        return this.#fetchAdvanced(this.#getAllWorksURL()).then((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })

    }

    addWork(work) {
        return this.#fetchAdvanced(this.#addWorkURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(work)
        }).them((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })
    }

    deleteWork(work) {
        return this.#fetchAdvanced(this.#deleteWorkURL(work), {
            method: 'DELETE'
        }).then((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })
    }

    updateWork(work) {
        return this.#fetchAdvanced(this.#updateWorkURL(work), {
            method: 'PUT',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(work)
        }).then((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON)[0];
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })
    }

    getWorkByDate(date) {
        return this.#fetchAdvanced(this.#getWorkByDateURL(date)).then((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })
    }

    getWorkByPeriod(start, end) {
        return this.#fetchAdvanced(this.#getWorkByPeriodURL(start, end)).then((responseJSON) => {
            let responseWork = WorkBO.fromJSON(responseJSON);
            return new Promise(function (resolve) {
                resolve(responseWork)
            })
        })
    }

    // Booking Methoden author Mihriban Dogan

    addTimeIntervalBooking(vacationBO) {
        return this.#fetchAdvanced(this.#addVacationURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(vacationBO)
        }).then((responseJSON) => {
            console.log("TEST")
            let responseBookingBO = VacationBO.fromJSON(responseJSON)[0];

            return new Promise(function (resolve) {
                resolve(responseBookingBO);
            })
        })
    }


    addBooking(bookingBO) {
        return this.#fetchAdvanced(this.#addTimeIntervalBookingURL(), {
            method: 'POST',
            headers: {
                'Accept': 'application/json, text/plain',
                'Content-type': 'application/json',
            },
            body: JSON.stringify(bookingBO)
        }).then((responseJSON) => {
            let responseBookingBO = BookingBO.fromJSON(responseJSON)[0];

            return new Promise(function (resolve) {
                resolve(responseBookingBO);
            })
        })
    }
}



