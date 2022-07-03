import React, { Component } from 'react';
import Button from '@mui/material/Button';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';

/**
 * @author Mihriban Dogan (https://github.com/mihriban-dogan)
 * Dialog zum löschen von Projekten
 */

class DeleteProject extends Component {
    constructor(props) {
        super(props);
    }

    

    deleteProject = () => {
      WorkTimeAppAPI.getAPI().deleteProject(this.props.project);
      this.props.onClose(this.props.project);

    }

    

    render() { 
        return (
            <Dialog open={this.props.show} onClose={this.handleClose}>
              <DialogTitle >{"Do you really want to delete your project?"}</DialogTitle>
              <DialogContent>
                <DialogContentText >
                If you click delete, your project and all members and activities will be deleted.</DialogContentText>
              </DialogContent>
              <DialogActions>
                <Button color="primary" onClick={this.props.onClose} >
                 Cancel
                </Button>
                <Button color="primary" onClick={this.deleteProject} autoFocus>
                  Delete
                </Button>
              </DialogActions>
            </Dialog>
          );
    }
}
 
export default DeleteProject;