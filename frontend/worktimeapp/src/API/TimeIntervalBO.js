import BusinessObject from './BusinessObject';

export default class TimeIntervalBO extends BusinessObject {
    constructor(type, breakId, illnessId, projectDurationId, projectWorkId, vacationId, workId){
        super();
        this.type = type;
        this.breakId = breakId;
        this.illnessId = illnessId;
        this.projectDurationId = projectDurationId;
        this.projectWorkId = projectWorkId;
        this.vacationId = vacationId;
        this.workId = workId;
    }

    setType(t){
        this.type = t;
    }

    getType(){
        return this.type;
    }

    setBreakId(id){
        this.breakId = id
    }

    getBreakId(){
        return this.breakId
    }

    setIllnessId(id){
        this.illnessId = id
    }

    getIllnessId(){
        return this.illnessId
    }

    setProjectDurationId(id){
        this.projectDurationId = id
    }

    getProjectDurationId(){
        return this.projectDurationId
    }

    setProjectWorkId(id){
        this.projectWorkId = id
    }

    getProjectWorkId(){
        return this.projectWorkId
    }

    setVacationId(id){
        this.vacationId = id
    }

    getVacationId(){
        return this.vacationId
    }

    setWorkId(id){
        this.workId = id
    }

    getWorkId(){
        return this.workId
    }

    static fromJSON(timeintervals){
        let res = [];
        if(Array.isArray(timeintervals)){
            timeintervals.forEach((ti) => {
                Object.setPrototypeOf(ti, TimeIntervalBO.prototype);
                res.push(ti)
            })
        }else{
            let ti = timeintervals;
            Object.setPrototypeOf(ti, TimeIntervalBO.prototype);
            res.push(ti)
        }
        return res;
    }
}