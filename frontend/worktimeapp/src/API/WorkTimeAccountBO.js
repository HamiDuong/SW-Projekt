import BusinessObject from './BusinessObject'

export default class WorkTimeAccountBO extends BusinessObject {
    constructor(userId, contractTime, overTime) {
        super();
        this.userId = userId;
        this.contractTime = contractTime;
        this.overTime = overTime;
    }

    //Getter und Setter
    setUserId(userId) {
        this.userId = userId;
    }

    getUserId() {
        return this.userId;
    }

    setContractTime(contractTime) {
        this.contractTime = contractTime;
    }

    getContractTime() {
        return this.contractTime;
    }

    setOverTime(overTime) {
        this.overTime = overTime;
    }

    getOverTime() {
        return this.overTime;
    }


    static fromJSON(workTimeAccountBO) {
        let res = [];
        if (Array.isArray(workTimeAccountBO)) {
            workTimeAccountBO.forEach((elem) => {
                Object.setPrototypeOf(elem, WorkTimeAccountBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = workTimeAccountBO;
            Object.setPrototypeOf(elem, WorkTimeAccountBO.prototype);
            res.push(elem)
        }
        return res;
    }
}