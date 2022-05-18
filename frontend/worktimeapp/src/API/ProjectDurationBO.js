import BusinessObject from "./BusinessObject";

export default class ProjectDuration extends BusinessObject{
    constructor(start, end, startEvent, endEvent, type, projectId){
        super();
        this.start = start;
        this.end = end;
        this.startEvent = startEvent;
        this.endEvent = endEvent;
        this.type = type;
        this.projectId = projectId;
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

    SetProjectId(id){
        this.projectId = id;
    }

    GetProjectId(){
        return this.projectId;
    }

    static fromJSON(duration){
        let res = [];
        if(Array.isArray(duration)){
            duration.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectDuration.prototype);
                res.push(elem)
            })
        }else{
            let elem = duration;
            Object.setPrototypeOf(elem, ProjectDuration.prototype);
            res.push(elem)
        }
        return res;
    }
}