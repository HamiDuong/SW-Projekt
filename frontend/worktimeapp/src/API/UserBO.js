import BusinessObject from './BusinessObject'

export default class UserBO extends BusinessObject {
    constructor(firstName, lastName, mailAdress, googleUserId) {
        super();
        this.firstName = firstName;
        this.lastName = lastName;
        this.mailAdress = mailAdress;
        this.googleUserId = googleUserId

    }

    //Getter und Setter
    setFirstName(firstName) {
        this.firstName = firstName;
    }

    getFirstName() {
        return this.firstName;
    }

    setLastName(lastName) {
        this.lastName = lastName;
    }

    getLastName() {
        return this.lastName;
    }

    setMailAdress(mailAdress) {
        this.mailAdress = mailAdress;
    }

    getMailAdress() {
        return this.mailAdress;
    }

    setGoogleUserId(googleUserId) {
        this.googleUserId = googleUserId;
    }

    getGoogleUserId() {
        return this.googleUserId;
    }



    static fromJSON(userBO) {
        let res = [];
        if (Array.isArray(userBO)) {
            userBO.forEach((elem) => {
                Object.setPrototypeOf(elem, UserBO.prototype);
                res.push(elem)
            })
        } else {
            let elem = userBO;
            Object.setPrototypeOf(elem, UserBO.prototype);
            res.push(elem)
        }
        return res;
    }
}