WITH ultimo_ano AS (
    SELECT *
    FROM demonstracoes_contabeis
    WHERE data >= CURRENT_DATE - INTERVAL '1 year'
)
SELECT 
    os.Registro_ANS,
    os.Razao_Social,
    os.Nome_Fantasia,
    SUM(dc.vl_saldo_final - dc.vl_saldo_inicial) AS total_despesas
FROM ultimo_ano dc
JOIN operadoras_saude os ON dc.reg_ans::TEXT = os.Registro_ANS::TEXT
WHERE dc.descricao ILIKE '%EVENTOS%SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
GROUP BY os.Registro_ANS, os.Razao_Social, os.Nome_Fantasia
ORDER BY total_despesas DESC
LIMIT 10;