import BusinessObject from '../BusinessObject'

export default class FlexDayEndBO extends BusinessObject {
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


    static fromJSON(flexdayendevent) {
        let res = [];
        if (Array.isArray(flexdayendevent)) {
            flexdayendevent.forEach((elem) => {
                Object.setPrototypeOf(elem, FlexDayEndBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = flexdayendevent;
            Object.setPrototypeOf(elem, FlexDayEndBO.prototype);
            res.push(elem)
        }
        return res;
    }
}