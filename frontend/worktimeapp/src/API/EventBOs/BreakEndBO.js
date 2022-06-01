import BusinessObject from '../BusinessObject'

export default class BreakStartBO extends BusinessObject {
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


    static fromJSON(breakendevent) {
        let res = [];
        if (Array.isArray(breakendevent)) {
            breakendevent.forEach((elem) => {
                Object.setPrototypeOf(elem, BreakStartBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = breakendevent;
            Object.setPrototypeOf(elem, BreakStartBO.prototype);
            res.push(elem)
        }
        return res;
    }
}