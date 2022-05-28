import BusinessObject from '../BusinessObject'

export default class VacationEndBO extends BusinessObject {
    constructor(time) {
        super();
        this.time = time
    }

    //Getter und Setter
    setTime(time) {
        this.time = time;
    }

    getTime() {
        return this.time;
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