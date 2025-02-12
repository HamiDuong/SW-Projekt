import BusinessObject from '../BusinessObject'

export default class IllnessStartBO extends BusinessObject {

    /**
   * IllnessStartBO:
   * Ereignis-Subklasse, die den Beginn einer Krankheitsspanne eines Mitarbeiters markiert. 
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


    static fromJSON(illnessstartevent) {
        let res = [];
        if (Array.isArray(illnessstartevent)) {
            illnessstartevent.forEach((elem) => {
                Object.setPrototypeOf(elem, IllnessStartBO.prototype);
                res.push(elem);
            })
        } else {
            let elem = illnessstartevent;
            Object.setPrototypeOf(elem, IllnessStartBO.prototype);
            res.push(elem);
        }
        return res;
    }
}