# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import log_pipeline_job_sample

import pytest

import test_constants as constants


@pytest.mark.usefixtures("mock_sdk_init", "mock_start_run")
def test_log_pipeline_job_sample(mock_log_pipeline_job, mock_pipeline_job):

    log_pipeline_job_sample.log_pipeline_job_sample(
        experiment_name=constants.EXPERIMENT_NAME,
        run_name=constants.EXPERIMENT_RUN_NAME,
        pipeline_job=mock_pipeline_job,
        project=constants.PROJECT,
        location=constants.LOCATION,
    )

    mock_log_pipeline_job.assert_called_with(pipeline_job=mock_pipeline_job)
