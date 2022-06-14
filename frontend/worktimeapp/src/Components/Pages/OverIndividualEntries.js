import React, { Component } from 'react';
import WorkTimeAppAPI from '../../API/WorkTimeAppAPI';
import IndividualEntry from './IndividualEntry';


class OverIndividualEntry extends Component {
    constructor(props) {
        super(props);
        this.state = ({
            projectId: this.props.value,
            activities: [],
            capacity: [],
            current_capacity: [],
            activity_names: [],
            userId: 1
        })
    }


    componentDidMount() {
        this.getActivitiesForProjectOfThisUser(this.props.value, this.state.userId)
        console.log(this.props.value)

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



    getActivitiesForProjectOfThisUser = (project_id, user_id) => {
        WorkTimeAppAPI.getAPI().getActivitiesByProjectForUser(project_id, user_id).then(activity =>
            this.setState({
                activities: [...this.state.activities, activity],
            }, this.checkActivities(activity),
                this.getCapacityofUserForProject(activity[0].id, this.state.userId)
            ))
    }

    checkActivities = (element) => {
        try {
            this.getCapacities(element);
            this.getActivityNames(element);



        } catch (e) {
            console.log(e);
        }
    }

    getCapacities = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            this.setState({
                capacity: [...this.state.capacity, arr[i].capacity]
            }, function () {
                console.log(this.state.capacity)
            })
            i = i + 1
        }
    }


    getActivityNames = (arr) => {
        const acti = this.state.activities
        let i = 0
        while (i <= acti.length) {
            this.setState({
                activity_names: [...this.state.activity_names, arr[i].name]
            }, function () {
                console.log('AN', this.state.activity_names)
            })
            i = i + 1
        }
    }

    render() {
        return (
            <div>
                {this.state.activities.map((element, index) => {
                    const value = element[index].id
                    return (
                        <div>
                            <IndividualEntry value={value} />
                        </div>
                    )
                })}
            </div>
        );
    }
}

export default OverIndividualEntry;