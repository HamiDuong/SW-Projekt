import BusinessObject from '../BusinessObject'

export default class IllnessStartBO extends BusinessObject {
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


    static fromJSON(illnessstartevent) {
        let res = [];
        if (Array.isArray(illnessstartevent)) {
            illnessstartevent.forEach((elem) => {
                Object.setPrototypeOf(elem, IllnessStartBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = illnessstartevent;
            Object.setPrototypeOf(elem, IllnessStartBO.prototype);
            res.push(elem)
        }
        return res;
    }
}