import BusinessObject from '../BusinessObject'

export default class FlexDayStartBO extends BusinessObject {

    /**
       * FlexDayStartBO:
       * Ereignis-Subklasse, die den Beginn des Überstundenabbaus eines Mitarbeiters markiert. 
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


    static fromJSON(flexdaystartevent) {
        let res = [];
        if (Array.isArray(flexdaystartevent)) {
            flexdaystartevent.forEach((elem) => {
                Object.setPrototypeOf(elem, FlexDayStartBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = flexdaystartevent;
            Object.setPrototypeOf(elem, FlexDayStartBO.prototype);
            res.push(elem);
        }
        return res;
    }
}