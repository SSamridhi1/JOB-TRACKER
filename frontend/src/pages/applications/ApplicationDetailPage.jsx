import { useParams } from 'react-router-dom'

// Skeleton page - will eventually call applicationService.getApplication(id)
// and render application details, status history, and notes.
function ApplicationDetailPage() {
  const { id } = useParams()

  return (
    <div>
      <h1>Application #{id}</h1>
      <p>Application details, status history, and notes will go here.</p>
    </div>
  )
}

export default ApplicationDetailPage
