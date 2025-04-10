document.addEventListener('DOMContentLoaded', function() {
    // Dane do wykresów
    const prognozaWzrostuData = {
        labels: ['2025 (GS)', '2025 (GVR)', '~2030'],
        datasets: [{
            label: 'Wartość Rynku AI (mld USD)',
            data: [158.4, 196, 2500],
            backgroundColor: [
                '#4e79a7', // Kolor dla GS
                '#f28e2b', // Kolor dla GVR
                '#e15759'  // Kolor dla ~2030
            ],
            borderColor: [
                '#4e79a7',
                '#f28e2b',
                '#e15759'
            ],
            borderWidth: 1
        }]
    };

    const inwestycjeData = {
        labels: ['Pryw. Inw. 2022', 'Fundusze do H1 2024'],
        datasets: [{
            label: 'Inwestycje w AI (mld USD)',
            data: [91.9, 249],
            backgroundColor: [
                '#59a14f', // Kolor dla Pryw. Inw. 2022
                '#76b7b2'  // Kolor dla Fundusze do H1 2024
            ],
            borderColor: [
                '#59a14f',
                '#76b7b2'
            ],
            borderWidth: 1
        }]
    };

    const adopcjaUEData = {
        labels: ['Dania', 'Szwecja', 'Belgia', 'Średnia UE', 'Polska*'],
        datasets: [{
            label: 'Adopcja AI w firmach (%)',
            data: [27.6, 25.0, 25.0, 13.5, 3.5], // Użyto 3.5 dla Polski jako reprezentatywnej wartości
            backgroundColor: [
                '#ff9da7', // Dania
                '#edc948', // Szwecja
                '#bab0ac', // Belgia
                '#e15759', // Średnia UE
                '#4e79a7'  // Polska
            ],
            borderColor: [
                '#ff9da7',
                '#edc948',
                '#bab0ac',
                '#e15759',
                '#4e79a7'
            ],
            borderWidth: 1
        }]
    };

    // Opcje wykresów (wspólne i specyficzne)
    const commonOptions = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    // Można dodać formatowanie ticków, jeśli potrzebne
                }
            },
            x: {
                 ticks: {
                    maxRotation: 0, // Zapobiega obracaniu etykiet, jeśli się mieszczą
                    minRotation: 0
                 }
            }
        },
        plugins: {
            legend: {
                display: false // Ukrywamy legendę, bo etykiety są na osiach lub w tytule
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        let label = context.dataset.label || '';
                        if (label) {
                            label += ': ';
                        }
                        if (context.parsed.y !== null) {
                            // Dodajemy jednostkę w zależności od wykresu
                            if (context.chart.canvas.id === 'adopcjaUEChart') {
                                label += context.parsed.y + '%';
                            } else {
                                label += context.parsed.y + ' mld USD';
                            }
                        }
                        return label;
                    }
                }
            }
        }
    };

    // Tworzenie wykresów
    const ctxPrognoza = document.getElementById('prognozaWzrostuChart').getContext('2d');
    new Chart(ctxPrognoza, {
        type: 'bar',
        data: prognozaWzrostuData,
        options: {
            ...commonOptions, // Rozszerzamy wspólne opcje
             plugins: { // Nadpisujemy/dodajemy pluginy specyficzne dla tego wykresu
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Prognoza Wzrostu Rynku AI (mld USD)'
                }
            }
        }
    });

    const ctxInwestycje = document.getElementById('inwestycjeChart').getContext('2d');
    new Chart(ctxInwestycje, {
        type: 'bar',
        data: inwestycjeData,
        options: {
            ...commonOptions,
             plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Inwestycje w AI (mld USD)'
                }
            }
        }
    });

    const ctxAdopcja = document.getElementById('adopcjaUEChart').getContext('2d');
    new Chart(ctxAdopcja, {
        type: 'bar',
        data: adopcjaUEData,
        options: {
            ...commonOptions,
            scales: { // Nadpisujemy skale dla tego wykresu
                 y: {
                    beginAtZero: true,
                    max: 30, // Ustawiamy maksimum osi Y dla lepszej czytelności
                    ticks: {
                        callback: function(value) {
                            return value + '%'; // Dodajemy znak % do etykiet osi Y
                        }
                    }
                },
                 x: {
                     ticks: {
                        maxRotation: 0,
                        minRotation: 0
                     }
                }
            },
             plugins: {
                ...commonOptions.plugins,
                title: {
                    display: true,
                    text: 'Adopcja AI w firmach w UE (2024, %)'
                },
                tooltip: { // Nadpisujemy tooltip dla tego wykresu
                    callbacks: {
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed.y !== null) {
                                label += context.parsed.y + '%'; // Zawsze dodajemy %
                            }
                            return label;
                        }
                    }
                }
            }
        }
    });

     // Dodajemy informację o Polsce do etykiety
     const adopcjaChart = Chart.getChart('adopcjaUEChart');
     if (adopcjaChart) {
         const polandLabelIndex = adopcjaChart.data.labels.findIndex(label => label === 'Polska*');
         if (polandLabelIndex !== -1) {
             // Można by dodać adnotację, ale prościej jest zostawić gwiazdkę i opis pod wykresem
             // console.log("Znaleziono etykietę Polski");
         }
     }

});