{{- define "mongodb.namespace" -}}
  {{- if .Values.global -}}
    {{- if .Values.global.namespaceOverride }}
      {{- .Values.global.namespaceOverride -}}
    {{- else -}}
      {{- .Release.Namespace -}}
    {{- end -}}
  {{- else -}}
    {{- .Release.Namespace -}}
  {{- end }}
{{- end -}}

{{- define "mongodb.fullname" -}}
  {{- .Release.Name -}}
{{- end }}

{{- define "mongodb.secretKeyRef" -}}
    {{- if .Values.auth.secretKeyRef -}}
        {{- printf "%s" .Values.auth.secretKeyRef -}}
    {{- else -}}
        {{- printf "%s-secret-key-ref" (include "mongodb.fullname" .) -}}
    {{- end -}}
{{- end -}}
