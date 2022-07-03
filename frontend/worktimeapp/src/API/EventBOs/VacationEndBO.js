import BusinessObject from '../BusinessObject'

export default class VacationEndBO extends BusinessObject {

    /**
   * VacationEndBO:
   * Ereignis-Subklasse, die das Ende des Urlaubs eines Mitarbeiters markiert. 
   * 
   * @author [Khadidja Kebaili] (https://github.com/khadidja-kebaili)
   */

    constructor(time, type) {
        super();
        this.time = time;
        this.type = type;
    }

    //Getter und Setter
    getTime() {
        return this.time
    }

    setTime(time) {
        this.time = time;
    }

    setType(type) {
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