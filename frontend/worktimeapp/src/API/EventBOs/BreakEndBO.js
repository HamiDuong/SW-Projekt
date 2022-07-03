import BusinessObject from '../BusinessObject'

export default class BreakEndBO extends BusinessObject {

    /**
    * BreakEndBO:
    * Ereignis-Subklasse, die das Ende einer Pause markiert. 
    * 
    * @author [Khadidja Kebaili] (https://github.com/khadidja-kebaili)
    */

    constructor(time) {
        super();
        this.time = time;
    }

    //Getter und Setter
    setTime(time) {
        this.time = time;
    }

    getTime() {
        return this.time;
    }


    static fromJSON(breakendevent) {
        let res = [];
        if (Array.isArray(breakendevent)) {
            breakendevent.forEach((elem) => {
                Object.setPrototypeOf(elem, BreakEndBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = breakendevent;
            Object.setPrototypeOf(elem, BreakEndBO.prototype);
            res.push(elem);
        }
        return res;
    }
}