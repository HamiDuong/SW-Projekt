import BusinessObject from '../BusinessObject'

export default class BreakStartBO extends BusinessObject {
    /**
   * BreakStartBO:
   * Ereignis-Subklasse, die den Beginn einer Pause markiert. 
   * 
   * @author [Khadidja Kebaili] (https://github.com/khadidja-kebaili)
   */

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


    static fromJSON(breakstartevent) {
        let res = [];
        if (Array.isArray(breakstartevent)) {
            breakstartevent.forEach((elem) => {
                Object.setPrototypeOf(elem, BreakStartBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = breakstartevent;
            Object.setPrototypeOf(elem, BreakStartBO.prototype);
            res.push(elem)
        }
        return res;
    }
}