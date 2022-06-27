import React, { Component } from 'react';
import AssignmentIcon from '@mui/icons-material/Assignment';

import {withStyles,
    Typography,
    Accordion,
    AccordionSummary,
    AccordionDetails,
    TextField,
    Button,
    List,
    ListItem,
    Box,
    Collapse,
    ListItemText,
    ListItemIcon,
    ListItemButton,
    ListSubheader,
    TableRow,
    TableHead,
    TableContainer,
    TableCell,
    TableBody,
    Table,
    Paper,
    FormControl,
    Card,
    Grid,
    Select,
    MenuItem,
    InputLabel
} from '@mui/material';

import { MyProjectpopup } from './MyProjectpopup';
import EditActivity from './Dialog/EditActivity';
import MyActivitiesEntry from './MyActivitiesEntry'
import WorkTimeAppAPI from '../API/WorkTimeAppAPI';

const header = [
  {
  id: 'name',
  name: 'Name',
  label: 'Name'
  },
  {
      id: 'commissioner',
      name: 'Commissioner',
      label: 'Commissioner'
  }, 
  {
      id: 'user',
      name: 'User',
      label: 'User'
  },
  {
      id: 'duration',
      name: 'Duration',
      label: 'Duration'
  },
]
const data = [
  {
      id: 1,
      name:'SW Project',
      commissioner: 'Thies',
      user: 'Susi',
      duration: '90 Tage'
  },
  {
      id: 2,
      name:'Programmieren',
      commissioner: 'Thies',
      user: 'Susi',
      duration: '999 Tage'
  },
  {
      id: 3,
      name:'Schlafen',
      commissioner: '',
      user: 'Susi',
      duration: '15 Tage'
  }
]

const activities = [
    {
        name: "Use Case erstellen",
        capacity: "45h"
    },
    {
        name: "ERM Diagram",
        capacity: "10h"
    },
    {
        name: "Blabla",
        capacity: "5h"
    },
]

/**
 * Projekte und Activities vom aktuellen User
 * 
 * @author [Vi Nam Le] (https://github.com/vinamle)
 */

class MyProjects extends Component {
    
    constructor(props) {
        super(props);

        this.state = {
          userId : props.userId,
          projects : null,
          projectuser: null,

          // projectType: "",
          // time: Date,

          showEditWindow: false,
          showEditActicity: false
      }

        //get Projects of current User
        //get Activities of these Projects
        /**
         * mögliche Form die Acticity Objekte zu holen:
         * {project id: [Liste der ActivityBOs]}
         */

  }

  editWindow = () => {
    this.setState({
      showEditWindow: true
    }, function(){
      console.log('Edit Window öffnen')
    })
  }

  closeDialog = (project) => {
    if(project){
      this.updateProject(project)
      this.setState({
        showEditWindow: false
      }, function(){
        console.log('Edit Window schließen')
      })
    }else{
      this.setState({
        showEditWindow:false
      }, function(){
        console.log('Edit Window schließen')
      })
    }
  }

  editWindowActivity = () => {
    this.setState({
      showEditActicity: true
    }, function(){
      console.log('Edit Window')
    })
  }

  closeDialogActivity = (activity) => {
    if(activity){
      this.updateProject(activity)
      this.setState({
        showEditActicity: false
      }, function(){
        console.log('Edit Window')
      })
    }else{
      this.setState({
        showEditWindow:false
      }, function(){
        console.log('Edit Window')
      })
    }
  }

  getProjects = () => {
    WorkTimeAppAPI.getAPI().getProjectUserByUserId(this.state.userId).then(projectuser =>   
      this.setState({
        projectuser : projectuser
      }, function(){
        console.log("API ProjectUser")
      })  
    )
    
    let resproject = []

    this.state.projectuser.forEach(elem => {
      WorkTimeAppAPI.getAPI().getProject(elem.getProjectId()).then(project =>
        resproject.append(project)
      )
    });

  }

  updateProject = (project) => {
    
  }

  // componentDidMount(){
  //   this.getProjects()
  // }

  render(){
    return(
      <Card sx={{ m:5, p:2, minwidth: 500}}>
        <Typography variant="h5" component="div">
          <AssignmentIcon></AssignmentIcon>
          My Projects
        </Typography>
        <Typography sx={{ fontSize: 16 }} color="text.secondary" gutterBottom>
          Your projects and activities at the moment. 
        </Typography>

        {data.map((item) => (
          <Accordion>
            <AccordionSummary>
              <TableRow>
                <TableCell>
                  {"Project name: "+item.name}
                </TableCell>
                <TableCell align="right">
                  {"Commisioner: "+item.commissioner}
                </TableCell>
              </TableRow>
            </AccordionSummary>
            <AccordionDetails>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>Activities</TableCell>
                    <TableCell align="left">Capacity</TableCell>
                    <TableCell></TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  <MyActivitiesEntry projectId = {item.id}></MyActivitiesEntry>
                </TableBody>
              </Table>
              <MyProjectpopup show={this.state.showEditWindow} onClose={this.closeDialog} project={item}></MyProjectpopup>
            </AccordionDetails>
          </Accordion>
        ))}
      </Card>
    )
  }
}
export default MyProjects