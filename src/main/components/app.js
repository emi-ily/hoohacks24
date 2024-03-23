export default function Logo() {
  return (
    <img
      src="{{ url_for('static', filename='terra_happy.png') }}"
      alt="Katherine Johnson"
    />
  )
}