import BusinessObject from '../BusinessObject'

export default class IllnessEndBO extends BusinessObject {
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


    static fromJSON(illnessendevent) {
        let res = [];
        if (Array.isArray(illnessendevent)) {
            illnessendevent.forEach((elem) => {
                Object.setPrototypeOf(elem, IllnessEndBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = illnessendevent;
            Object.setPrototypeOf(elem, IllnessEndBO.prototype);
            res.push(elem)
        }
        return res;
    }
}