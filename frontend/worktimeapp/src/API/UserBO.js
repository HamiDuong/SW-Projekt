import BusinessObject from './BusinessObject';

export default class UserBO extends BusinessObject {


  constructor(firstName, lastName, mailAdress, googleUserID ) {
    super();
    this.firstName = firstName
    this.lastName = lastName
    this.mailAdress = mailAdress
    this.googleUserID = googleUserID
  }


  setFirstName(firstName) {
    this.firstName = firstName
  }

  
  getFirstName() {
    return this.firstName
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

  setGoogleUserId(googleUserID) {
    this.googleUserID = googleUserID;
  }
  getGoogleUserId() {
    return this.googleUserID;
  }

  
  


  
  static fromJSON(bookings) {
    let result = [];

    if (Array.isArray(bookings)) {
      bookings.forEach((b) => {
        Object.setPrototypeOf(b, UserBO.prototype);
        result.push(b);
      })
    } else {
      // Es handelt sich offenbar um ein singuläres Objekt
      let b = bookings;
      Object.setPrototypeOf(b, UserBO.prototype);
      result.push(b);
    }

    return result;
  }
}