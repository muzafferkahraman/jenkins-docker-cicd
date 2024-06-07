pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        sh 'docker build -t my-flask-app .'
        sh 'docker tag my-flask-app $DOCKER_BFLASK_IMAGE'
      }
    }
    stage('Test') {
      steps {
        sh 'docker run my-flask-app python -m pytest app/tests/'
      }
    }
    stage('Deploy') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKER_REGISTRY_CREDS}", passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
          sh "echo \$DOCKER_PASSWORD | docker login -u \$DOCKER_USERNAME --password-stdin docker.io"
          sh 'docker push $$DOCKER_BFLASK_IMAGE'
        }
        sshagent(['${SSH_CREDENTIALS_ID}']) {
          sh """
            ssh ${SSH_REMOTE_HOST} <<EOF
              docker stop my-flask-app || true
              docker rm my-flask-app || true
              docker pull ${DOCKER_BFLASK_IMAGE}
              docker run -d --name my-flask-app -p 5000:5000 ${DOCKER_BFLASK_IMAGE}
            EOF
          """
        }
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
