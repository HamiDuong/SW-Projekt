import BusinessObject from './BusinessObject';

export default class UserBO extends BusinessObject {


  constructor(first_name, lastname, mailadress, username ) {
    super();
    this.first_name = first_name
    this.last_name = lastname
    this.mail_adress = mailadress
    this.user_name = username
  }


  setfirstname(firstname) {
    this.firstname = firstname
  }

  
  getfirstname() {
    return this.firstname
  }


  setlastname(lastname) {
    this.lastname = lastname;
  }


  getlastname() {
    return this.lastname;
  }

  
  getmailadress() {
    return this.mailadress;
  }

  setmailadress(mailadress) {
    this.mailadress = mailadress;
  }


  getusername() {
    return this.username;
  }

  setusername(username) {
    this.username = username;
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