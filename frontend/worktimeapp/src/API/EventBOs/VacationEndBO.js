import BusinessObject from '../BusinessObject'

export default class VacationEndBO extends BusinessObject {
    constructor(time, type) {
        super();
        this.time = time,
        this.type = type
    }

    //Getter und Setter
    getTime(time) {
        this.time = time;
    }

    setTime(time) {
        this.time = time;
    }

    setType() {
        this.type = type;
    }

    getType() {
        return this.type;
    }


    static fromJSON(vacationendevent) {
        let res = [];
        if (Array.isArray(vacationendevent)) {
            vacationendevent.forEach((elem) => {
                Object.setPrototypeOf(elem, VacationEndBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = vacationendevent;
            Object.setPrototypeOf(elem, VacationEndBO.prototype);
            res.push(elem)
        }
        return res;
    }
}