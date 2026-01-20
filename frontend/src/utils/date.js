export const formatReadableDate = (dateString) => {
    const hasTime = dateString.includes("T");

    const options = hasTime
      ? {
          weekday: "long",
          day:"numeric",
          month: "long",
          year: "numeric",
          hour: "2-digit",
          minute: "2-digit",
          hour12: false
        }
      : {
          day:"numeric",
          month: "long",
          year: "numeric",
        };

    return new Date(dateString).toLocaleString("es-CO", options).replace(" de ", " ");
}

export const formatDateTime = (dateString) =>
    new Date(dateString).toLocaleString("es-CO");
