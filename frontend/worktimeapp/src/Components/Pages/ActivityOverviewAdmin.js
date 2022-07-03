import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import Entry from './ActivityEntriesAdmin';
import Alert from '@mui/material/Alert';

/**
 * @author Khadidja Kebaili (https://github.com/KhadidjaKebaili)
 * Komponente für die Aktivitätsüberschau der Projektmitglieder für den Admin
 */
class ActivityOverviewAdmin extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            projectId: this.props.value,
            activities: [],
            capacity: [],
            current_capacity: [],
            activity_names: [],
            userId: this.props.userId,
            activities_vorhanden: false,
            selectedProject: '',
        })
    }

    // Aktivitäten für das Projekt holen
    getActivitiesForProject = (project) => {
        WorkTimeAppAPI.getAPI().getActivitiesByProjectId(project).then(activity =>
            this.setState({
                activities: [...this.state.activities, activity],
            }, this.checkActivities(activity)
            ))
    }

    // Kapazitäten der Projektuser holen
    getCapacityofUserForProject = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(activity =>
            this.setState({
                current_capacity: [...this.state.current_capacity, activity],
            }, function () {
                console.log(this.state.current_capacity)
            }
            ))
    }

    // Kapazitäten holen
    getCapacities = (arr) => {
        const acti = this.state.activities;
        let i = 0;
        while (i <= acti.length) {
            this.setState({
                capacity: [...this.state.capacity, arr[i].capacity]
            }, function () {
                console.log(this.state.capacity)
            })
            i = i + 1
        }
    }

    // Aktivitätsnamen holen    
    getActivityNames = (arr) => {
        const acti = this.state.activities;
        let i = 0;
        while (i <= acti.length) {
            this.setState({
                activity_names: [...this.state.activity_names, arr[i].name]
            }, function () {
                console.log('AN', this.state.activity_names)
            })
            i = i + 1
        }
    }

    // Prüfen ob es eine valide Aktivität ist
    checkActivities = (element) => {
        try {
            this.getCapacities(element);
            this.getActivityNames(element);
            this.setState({ activities_vorhanden: true })
            this.getCapacityofUserForProject(element[0].id, this.state.userId);
        } catch (e) {
            console.log(e);

        }
    }

    componentDidMount() {
        this.getActivitiesForProject(this.props.value);
    }


    showEntries() {
        let len = this.state.activities.length;
        let liste = this.state.activities[0];
        if (this.state.activities_vorhanden) {
            return (
                <div>
                    {liste.map((element) => {
                        const value = element.id
                        return (
                            <Entry projectId={this.state.projectId} value={value} />
                        )
                    })}
                </div>
            )
        } else {
            return (
                console.log('No entries yet.')
            )
        }
    }


    render() {
        return (
            <div>
                {
                    this.state.activities_vorhanden ?
                        this.showEntries()
                        : <div>
                            <Alert sx={{ margin: 3 }} variant='outlined' severity="info">There are no activities for your project yet.</Alert>
                        </div>
                }
            </div>
        );
    }
}

export default ActivityOverviewAdmin;