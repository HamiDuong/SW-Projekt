import BusinessObject from "./BusinessObject";

export default class ProjectWorkBO extends BusinessObject{
    constructor(start, end, startEvent, endEvent, type, activityId){
        super();
        this.start = start;
        this.end = end;
        this.startEvent = startEvent;
        this.endEvent = endEvent;
        this.type = type;
        this.activitytId = activityId;
    }

    //Getter und Setter
    SetStart(start){
        this.start = start;
    }

    GetStart(){
        return this.start;
    }

    SetEnd(end){
        this.end = end;
    }

    GetEnd(){
        return this.end;
    }

    SetStartEvent(sEvent){
        this.startEvent = sEvent;
    }

    GetStartEvent(){
        return this.startEvent;
    }

    SetEndEvent(eEvent){
        this.endEvent = eEvent;
    }

    GetEndEvent(){
        return this.endEvent;
    }
    
    SetType(type){
        this.type = type;
    }

    GetType(){
        return this.type;
    }

    SetActivityId(id){
        this.activitytId = id;
    }

    GetActivityId(){
        return this.activitytId;
    }

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