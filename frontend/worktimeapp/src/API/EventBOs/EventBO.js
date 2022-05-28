import BusinessObject from '../BusinessObject'

export default class EventBO extends BusinessObject {
    constructor(type, comingId, goingId, vacationStartId, vacationEndId, projectWorkStartId, projectWorkEndId,
        breakEndId, breakStartId, flexDayStartId, flexDayEndId, illnessEndId, illnessStartId) {
        super();
        this.type = type,
            this.ComingId = comingId,
            this.GoingId = goingId,
            this.VacationStartId = vacationStartId,
            this.VacationEndId = vacationEndId,
            this.IllnessStartId = illnessStartId,
            this.IllnessEndId = illnessEndId,
            this.ProjectWorkEndId = projectWorkEndId,
            this.ProjectWorkStartId = projectWorkStartId,
            this.BreakStartId = breakStartId,
            this.BreakEndId = breakEndId,
            this.FlexDayEndId = flexDayEndId,
            this.FlexDayStartId = flexDayStartId
    }

    //Getter und Setter
    setType(type) {
        this.type = type;
    }

    getType() {
        return this.type;
    }

    setComingId(comingId) {
        this.ComingId = comingId
    }

    getComingId() {
        return this.ComingId
    }

    setGoingId(goingId) {
        this.GoingId = goingId
    }

    getGoingId() {
        return this.GoingId
    }

    setProjectWorkEndId(projectWorkEndId) {
        this.ProjectWorkEndId = projectWorkEndId
    }

    getProjectWorkEndId() {
        return this.ProjectWorkEndId
    }

    setProjectWorkStartId(projectWorkStartId) {
        this.ProjectWorkStartId = projectWorkStartId
    }

    getProjectWorkStartId() {
        return this.ProjectWorkStartId
    }

    setVacationStartId(vacationStartId) {
        this.VacationStartId = vacationStartId
    }

    getVacationStartId() {
        return this.VacationStartId
    }

    setVacationEndId(vacationEndId) {
        this.VacationEndId = vacationEndId
    }

    getVacationEndId() {
        return this.VacationEndId
    }

    setBreakStartId(breakStartId) {
        this.BreakStartId = breakStartId
    }

    getBreakStartId() {
        return this.BreakStartId
    }

    setBreakStartId(breakStartId) {
        this.BreakStartId = breakStartId
    }

    getBreakStartId() {
        return this.BreakStartId
    }

    setFlexDayStartId(flexDayStartId) {
        this.FlexDayStartId = flexDayStartId
    }

    getFlexDayStartId() {
        return this.FlexDayStartId
    }

    setFlexDayEndId(flexDayEndId) {
        this.FlexDayEndId = flexDayEndId
    }

    getFlexDayEndId() {
        return this.FlexDayEndId
    }


    static fromJSON(event) {
        let res = [];
        if (Array.isArray(event)) {
            event.forEach((elem) => {
                Object.setPrototypeOf(elem, EventBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = event;
            Object.setPrototypeOf(elem, EventBO.prototype);
            res.push(elem)
        }
        return res;
    }
}