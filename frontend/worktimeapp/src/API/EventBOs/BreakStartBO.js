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