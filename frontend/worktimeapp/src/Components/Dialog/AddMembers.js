import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';



class AddMembers extends Component {
  constructor(props) {
    super(props);
     this.state={
      projectID: '',
      userId: '',
      capacity: null,
      selectedUser: false,
      targetUser: [],
      userName:'',
      

  }
  
     }
  getNamesForProject = async () => {
    const {userName} = this.state;
    console.log(this.state.userName)
        WorkTimeAppAPI.getAPI().searchUser(userName).then(userBO =>
          this.setState({
            users: [userBO],
            

          }, function(){
            console.log(this.state.userName)
          }
          ))
        }
  
        handle(e) {
          this.setState({
            event: e.target.value,
            selectedUser: true,
            userId: e.target.value
            
          }, console.log(this.state.userId));
        }
  
       componentDidMount() {
        this.getNamesForProject(1)
       } 


  state = {  }
  render() { 
    return ( 
      <div>
        Hallo Läuft!
      </div>
     );
  }
}
 
export default AddMembers;