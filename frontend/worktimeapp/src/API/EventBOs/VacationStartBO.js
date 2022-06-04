import BusinessObject from '../BusinessObject'

export default class VacationStartBO extends BusinessObject {
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


    static fromJSON(vacationstartevent) {
        let res = [];
        if (Array.isArray(vacationstartevent)) {
            vacationstartevent.forEach((elem) => {
                Object.setPrototypeOf(elem, VacationStartBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = vacationstartevent;
            Object.setPrototypeOf(elem, VacationStartBO.prototype);
            res.push(elem)
        }
        return res;
    }
}