import BusinessObject from "./BusinessObject";

/**
 * Businessobject von ProjectUser
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */
export default class ProjectUser extends BusinessObject{
    constructor(projectId, userId, capacity, currentCapacity){
        super();
        this.projectId = projectId;
        this.userId = userId;
        this.capacity = capacity;
        this.currentCapacity = currentCapacity;
    }

    //Getter und Setter

    setProjectId(id){
        this.projectId = id;
    }

    getProjectId(){
        return this.projectId;
    }


    setUserId(userId){
        this.userId = userId;
    }

    getUserId(){
        return this.userId;
    }

    setCapacity(capacity){
        this.capacity = capacity;
    }

    getCapacity(){
        return this.capacity;
    }

    setCurrentCapacity(capacity){
        this.currentCapacity = capacity;
    }

    getCurrentCapacity(){
        return this.currentCapacity;
    }

    SetCurrentCapacity(currentCapacity){
        this.currentCapacity = currentCapacity;
    }

    GetCurrentCapacity(){
        return this.currentCapacity;
    }


    static fromJSON(projectuser){
        let res = [];
        if(Array.isArray(projectuser)){
            projectuser.forEach((elem) => {
                Object.setPrototypeOf(elem, ProjectUser.prototype);
                res.push(elem);
            })
        }else{
            let elem = projectuser;
            Object.setPrototypeOf(elem, ProjectUser.prototype);
            res.push(elem);
        }
        return res;
    }
}