import BusinessObject from '../BusinessObject'

export default class VacationStartBO extends BusinessObject {

    /**
   * VacationStartBO:
   * Ereignis-Subklasse, die den Beginn des Urlaubs eines Mitarbeiters markiert. 
   * 
   * @author [Khadidja Kebaili] (https://github.com/khadidja-kebaili)
   */

    constructor(time, type) {
        super();
        this.time = time;
        this.type = type;
    }

    //Getter und Setter
    setTime(time) {
        this.time = time;
    }

    getTime() {
        return this.time;
    }

    setType(type) {
        this.type = type;
    }

    getType() {
        return this.type;
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