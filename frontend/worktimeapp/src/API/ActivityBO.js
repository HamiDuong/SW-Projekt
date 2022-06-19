import BusinessObject from "./BusinessObject";

export default class Activity extends BusinessObject{
    constructor(name, capacity, projectId, currentCapacity){
        super();
        this.name = name;
        this.capacity = capacity;
        this.projectId = projectId;
        this.currentCapacity = currentCapacity;
    }

    //Getter und Setter
    SetName(name){
        this.name = name;
    }

    GetName(){
        return this.name;
    }

    SetCapacity(capacity){
        this.capacity = capacity;
    }

    GetCapacity(){
        return this.capacity;
    }

    SetProjectId(id){
        this.projectId = id;
    }

    GetProjectId(){
        return this.projectId;
    }

    SetCurrentCapacity(currentCapacity){
        this.currentCapacity = currentCapacity
    }

    GetCurrentCapacity(){
        return this.currentCapacity;
    }

    static fromJSON(activity){
        let res = [];
        if(Array.isArray(activity)){
            activity.forEach((elem) => {
                Object.setPrototypeOf(elem, Activity.prototype);
                res.push(elem)
            })
        }else{
            let elem = activity;
            Object.setPrototypeOf(elem, Activity.prototype);
            res.push(elem)
        }
        return res;
    }
}