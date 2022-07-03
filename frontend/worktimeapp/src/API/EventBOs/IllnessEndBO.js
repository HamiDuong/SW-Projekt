import BusinessObject from '../BusinessObject'

export default class IllnessEndBO extends BusinessObject {

    /**
   * IllnessEndBO:
   * Ereignis-Subklasse, die das Ende einer Krankheitsspanne eines Mitarbeiters markiert. 
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
