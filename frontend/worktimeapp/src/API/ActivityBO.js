import BusinessObject from "./BusinessObject";

/**
 * Businessobject von Actibity
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */
export default class Activity extends BusinessObject {
    constructor(name, capacity, projectId, currentCapacity) {
        super();
        this.name = name;
        this.capacity = capacity;
        this.projectId = projectId;
        this.currentCapacity = currentCapacity;
    }

    //Getter und Setter
    setName(name) {
        this.name = name;
    }

    getName() {
        return this.name;
    }

    setCapacity(capacity) {
        this.capacity = capacity;
    }

    getCapacity() {
        return this.capacity;
    }

    setProjectId(id) {
        this.projectId = id;
    }

    getProjectId() {
        return this.projectId;
    }

    setCurrentCapacity(currentCapacity) {
        this.currentCapacity = currentCapacity;
    }

    getCurrentCapacity() {
        return this.currentCapacity;
    }

    static fromJSON(activity) {
        let res = [];
        if (Array.isArray(activity)) {
            activity.forEach((elem) => {
                Object.setPrototypeOf(elem, Activity.prototype);
                res.push(elem);
            })
        } else {
            let elem = activity;
            Object.setPrototypeOf(elem, Activity.prototype);
            res.push(elem);
        }
        return res;
    }
}