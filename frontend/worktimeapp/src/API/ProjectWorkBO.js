import BusinessObject from "./BusinessObject";

/**
 * @author Ha Mi Duong (https://github.com/HamiDuong)
 * 
 * Objekt für Projektarbeitszeit
 */
export default class ProjectWorkBO extends BusinessObject{
    constructor(start, end, startEvent, endEvent, type, activityId){
        super();
        this.start = start;
        this.end = end;
        this.startEvent = startEvent;
        this.endEvent = endEvent;
        this.type = type;
        this.activityId = activityId;
    }

    // Getter und Setter
    setStart(start){
        this.start = start;
    }

    getStart(){
        return this.start;
    }

    setEnd(end){
        this.end = end;
    }

    getEnd(){
        return this.end;
    }

    setStartEvent(sEvent){
        this.startEvent = sEvent;
    }

    getStartEvent(){
        return this.startEvent;
    }

    setEndEvent(eEvent){
        this.endEvent = eEvent;
    }

    getEndEvent(){
        return this.endEvent;
    }
    
    setType(type){
        this.type = type;
    }

    getType(){
        return this.type;
    }

    setActivityId(id){
        this.activityId = id;
    }

    getActivityId(){
        return this.activityId;
    }

    // wandelt JSON in ProjectWorkBO
    static fromJSON(pWork){
        let res = [];
        if(Array.isArray(pWork)){
            pWork.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectWorkBO.prototype);
                res.push(elem)
            })
        }else{
            let elem = pWork;
            Object.setPrototypeOf(elem, ProjectWorkBO.prototype);
            res.push(elem)
        }
        return res;
    }
}