import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import IndividualEntry from './ActivityEntries';
import Alert from '@mui/material/Alert';


class ActivityOverview extends Component {
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
        })
    }

    getActivitiesForProject = (project) => {
        WorkTimeAppAPI.getAPI().getActivitiesByProjectId(project).then(activity =>
            this.setState({
                activities: [...this.state.activities, activity],
            }, this.checkActivities(activity)
            ))
    }


    getCapacityofUserForProject = (act_id, us_id) => {
        WorkTimeAppAPI.getAPI().getBookedTimeOfUserForAnActivity(act_id, us_id).then(activity =>
            this.setState({
                current_capacity: [...this.state.current_capacity, activity],
            }, function () {
                console.log(this.state.current_capacity)
            }
            ))
    }


    getCapacities = (arr) => {
        const acti = this.state.activities;
        for (let i = 0; i <= acti.length; i++) {
            this.setState({
                capacity: [...this.state.capacity, arr[i].getCapacity()]
            }, function () {
                console.log(this.state.capacity)
            })
        }
    }


    getActivityNames = (arr) => {
        const acti = this.state.activities;
        for (let i = 0; i <= acti.length; i++) {
            this.setState({
                activity_names: [...this.state.activity_names, arr[i].getName()]
            }, function () {
                console.log('Callback function', this.state.activity_names)
            })
        }
    }

    checkActivities = (element) => {
        try {
            this.getCapacities(element);
            this.getActivityNames(element);
            this.setState({ activities_vorhanden: true });
            this.getCapacityofUserForProject(element[0].getId(), this.state.userId);

        } catch (e) {
            console.log(e);

        }
    }

    componentDidMount() {
        this.getActivitiesForProject(this.props.value);
    }


    showing() {
        let len = this.state.activities.length;
        let liste = this.state.activities[0];
        if (this.state.activities_vorhanden == true) {
            return (
                <div>
                    {liste.map((element) => {
                        const value = element.id
                        return (
                            <IndividualEntry projectId={this.state.projectId} value={value} us_id={this.state.userId} />
                        )
                    })}
                </div>
            )
        } else {
            return (
                <div> Keine Aktivitäten vorhanden</div>
            )
        }
    }


    render() {
        return (
            <div>
                {
                    this.state.activities_vorhanden ?
                        this.showing()
                        : <div>
                            <Alert sx={{ margin: 3 }} variant='outlined' severity="info">There are no activities for your project yet.</Alert>
                        </div>
                }
            </div>
        );
    }
}
export default ActivityOverview;