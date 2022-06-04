import React, { Component } from 'react';
import { withStyles, Typography, Paper } from '@material-ui/core';
import WorkTimeAppAPI from './../API/WorkTimeAppAPI';
import UserBO from '../API/UserBO';



class CreateMyProfile extends Component {

    constructor(props) {
      super(props);
  
      // Init state
      this.state = {
        user: '',
        id: 1,
        dateOfLastChange : 0,
         first_name:"",
         last_name:"",
         mail_adress:"",
         user_name:"",
        loadingInProgress: false,
        loadingError: null,
      };
    }
  
    /** Lifecycle method, which is called when the component gets inserted into the browsers DOM */
    componentDidMount() {
      this.getUser();
    }
  
    /** gets the balance for this account */
    getUser = () => {
      WorkTimeAppAPI.getAPI().getUserById(this.props.id).then(user =>
        this.setState({
          user: user,
        })).catch(e =>
          this.setState({ // Reset state with error from catch 
            user: null,
          })
        );
  
    }

    getUsers = () => {
        WorkTimeAppAPI.getAPI().getUserById(1).then(vacationBOs =>
            this.setState({  
                user: vacationBOs,
            }, function(){
                console.log(this.state.user)
            }))
    }

    componentDidMount() {
    this.getUsers()}

  
    /** Renders the component */
    render() {
      const { id, dateOfLastChange, first_name, last_name, mail_adress, user_name } = this.state;
  
      return (
        <Paper variant='outlined' first_name={first_name}>
  
          <Typography variant='h6'>
            User
          </Typography>
          <Typography>
            ID: {id}
          </Typography>
          {
            user ?
              <Typography>
                User: {user.getLastName()}, {user.getFirstName()}
              </Typography>
              : null
          }
          </Paper>
      );
    }
  }
  
  /** Component specific styles */
  const styles = theme => ({
    root: {
      width: '100%',
      padding: theme.spacing(1),
      marginTop: theme.spacing(1)
    },
    accountEntry: {
      fontSize: theme.typography.pxToRem(15),
      flexBasis: '33.33%',
      flexShrink: 0,
    }
  });

  export default withStyles(styles)(CreateMyProfile);